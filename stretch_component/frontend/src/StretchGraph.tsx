import React, { useEffect, useState, useRef } from "react";
import { Streamlit, withStreamlitConnection, ComponentProps } from "streamlit-component-lib";
import { SVG , Svg, Timeline, Circle, Text, Line, Color} from '@svgdotjs/svg.js'

class Node{
  value:any;
  x:number;
  y:number;
  parent:Node | null;
  circle:Circle | null;
  letter:Text | null;
  line:Line | null;
  constructor(value:any, x:number, y:number){
    this.value = value;
    this.x = x;
    this.y = y;
    this.parent = null;
    this.circle = null;
    this.letter = null;
    this.line = null;
  }
}

function createCircle(nodo:Node, canvas:Svg, left:boolean, timeline:Timeline, radius:number, lenCircus:number){
  let circle = canvas.circle(2*radius).move(2*radius*nodo.x,2*radius*nodo.y + radius/2);
  circle.fill('none')
  circle.stroke({
    color: '#203357',
    width: 6,
    dasharray: [lenCircus].toString(),
    dashoffset: lenCircus,
    linecap: 'round'
  }).timeline(timeline);

  if(!left){
    circle.transform({rotate: 315,scaleY: -1})
  }else{
    circle.transform({rotate: 225});
  }
  
  nodo.circle = circle;

  return circle;
}

function createLetter(nodo:Node, canvas:Svg, timeline:Timeline, txSize:number, radius:number, theme:string){
  let txt = canvas.text(nodo.value.toString()).font({
    family: 'Helvetica', size: txSize, opacity: 0
  })
  console.log(theme)
  if(theme == "dark"){
    txt.fill("white");
  }else{
    txt.fill("black");
  }
  txt.move(2*radius*nodo.x + radius-  (txt.text().length)*(0.5)*(txt.length()/(txt.text().length)),radius/2.5 + 2*radius*nodo.y + radius/2).timeline(timeline);
  nodo.letter = txt;
  return txt;
}

function createLine(nodo:Node | undefined, timeline:Timeline, radius:number, canvas:Svg, setColor:string = "#203357"){
  if(nodo?.parent){
    let xprev = nodo.parent.x;
    let yprev = nodo.parent.y;
    let fromNode:number[],toNode:number[];
    let aux =(radius*Math.SQRT2)/2;
    if(xprev < nodo.x){
      fromNode = [radius*(2*xprev+1) + aux, radius*(2*yprev + 1) + aux + radius/2];
      toNode = [radius*(2*nodo.x+1) - aux,radius*(2*nodo.y+1) -aux + radius/2];
    }else{
      fromNode = [radius*(2*xprev+1) - aux, radius*(2*yprev + 1) + aux + radius/2];
      toNode = [radius*(2*nodo.x+1) + aux, radius*(2*nodo.y+1) - aux + radius/2];
    }
    let ln = canvas.line().plot([fromNode[0],fromNode[1],fromNode[0],fromNode[1]]).stroke(
      { color: setColor, width: 6, linecap: 'round',opacity: 0 }
    ).timeline(timeline).remember({
      from : fromNode,
      to : toNode
    });
    nodo.line = ln;
    return ln;
  }
  return canvas.line();
}

const StretchGraph = (props: ComponentProps) => {
  
  const {radius, speed, numberOfNodes, theme, key} = props.args;
  const lenCircle = 2*radius*Math.PI;
  const mainWidth = 2*(numberOfNodes+5)*radius;
  const mainHeight = 2*(numberOfNodes)*radius + radius;
  
  const myTime = new Timeline().persist(true)
  myTime.on('finished', (e) => {
    myTime.stop();
    myTime.play();
  })
  const svgRef = useRef<HTMLDivElement | null>(null);
  const drawRef = useRef<Svg | null>(null);

  useEffect(() => Streamlit.setFrameHeight());
  useEffect(() => {
    if (svgRef.current) {
      const draw = SVG().addTo(svgRef.current).size('100%', '100%');
      drawRef.current = draw;
      let nodes:Node[] = [];
      let circles:Circle[] = [];
      let texts:Text[] = [];
      let lines:Line[] = [];
      
      if(numberOfNodes > 0){
        nodes.push(new Node(0,2,0));
        circles.push(createCircle(nodes[0],draw,true,myTime,radius,lenCircle));
        circles[0].animate(speed,0,'after').ease('<>').stroke({dashoffset: 0});
        texts.push(createLetter(nodes[0],draw,myTime,radius,radius,theme));
        texts[0].animate(speed*3/4,0,'after').ease('<>').font({opacity: 1});
      }
      
      for(let i:number = 1;i<numberOfNodes;i++){
        nodes.push(new Node(i,i+2,i));
        nodes[i].parent = nodes[i-1];
        lines.push(createLine(nodes[i],myTime,radius,draw));
        lines[i-1].animate(1,0,'after').stroke({opacity:1});
        lines[i-1].animate(speed*3/4,0,'after').ease('<>').plot([lines[i-1].remember("from"),lines[i-1].remember("to")]);
        circles.push(createCircle(nodes[i],draw,true,myTime,radius,lenCircle));
        circles[i].animate(speed,0,'after').ease('<>').stroke({dashoffset: 0});
        texts.push(createLetter(nodes[i],draw,myTime,radius,radius,theme));
        texts[i].animate(speed*3/4,0,'after').ease('<>').font({opacity: 1});
      }

      return () => {
        drawRef.current?.remove();  
      };
    }
  }, [theme]);

  return (
    <>
      <div ref={svgRef} style={{ width: mainWidth.toString() + "px", height: mainHeight.toString() + "px", margin: "auto"}}>
      </div>
    </>
  );
};

export default withStreamlitConnection(StretchGraph) ;