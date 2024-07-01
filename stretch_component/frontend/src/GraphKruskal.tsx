import React, { useEffect, useState, useRef } from "react";
import { Streamlit, withStreamlitConnection, ComponentProps } from "streamlit-component-lib";
import { SVG , Svg, Timeline, Circle, Text, Line, Color, List, Gradient} from '@svgdotjs/svg.js'

class Node{
    value:any;
    key:number;
    x:number;
    y:number;
    circle:Circle | null;
    letter:Text | null;
    constructor(value:any, x:number, y:number,key:number){
      this.value = value;
      this.key = key;
      this.x = x;
      this.y = y;
      this.circle = null;
      this.letter = null;
    }
  }

class Edge{
    line:Line | null;
    terminalA:Node;
    terminalB:Node;
    weight:number;
    letter:Text | null;
    constructor(nodoa:Node,nodob:Node,weight:number){
        this.line = null;
        this.terminalA = nodoa;
        this.terminalB = nodob;
        this.weight = weight;
        this.letter = null;
    }
}

class Graph{
    adjList:Map<Node,Edge[]>;
    adjMatrix:number[][];
    constructor(){
      this.adjList = new Map<Node,Edge[]>();
      this.adjMatrix = [];
    }

    generateMatrix(){
      for(let i = 0; i < this.adjList.size; i++){ 
        this.adjMatrix[i] = new Array(this.adjList.size).fill(0); 
      }
    }

    addNode(nodo:Node){
      this.adjList.set(nodo, []);
    }

    existsEdge(nodeA:Node,nodeB:Node){
      return this.adjMatrix[nodeA.key][nodeB.key] >= 1;
    }

    addEdge(edge:Edge){
      if(!this.existsEdge(edge.terminalA,edge.terminalB)){
        this.adjList.get(edge.terminalA)?.push(edge);
        this.adjMatrix[edge.terminalA.key][edge.terminalB.key] = edge.weight;
        this.adjList.get(edge.terminalB)?.push(edge);
        this.adjMatrix[edge.terminalB.key][edge.terminalA.key] = edge.weight;
      }
    }

    deleteEdge(edge:Edge){
      let arr1 = this.adjList.get(edge.terminalA);
      let arr2 = this.adjList.get(edge.terminalB);
      this.adjMatrix[edge.terminalA.key][edge.terminalB.key] = 0;
      this.adjMatrix[edge.terminalB.key][edge.terminalA.key] = 0;
      let safeEdge;
      if(arr1){
        while(arr1.slice(-1)[0] != edge){
          safeEdge = arr1.pop();
          if(safeEdge){
            arr1.unshift(safeEdge);
          }
        }
        arr1.pop();
      }
      if(arr2){
        while(arr2.slice(-1)[0] != edge){
          safeEdge = arr2.pop();
          if(safeEdge){
            arr2.unshift(safeEdge);
          }
        }
        arr2.pop();
      }
    }

    printList(){
      console.log("Imprimiendo lista: ")
      this.adjList.forEach((value:Edge[],key:Node)=>{
        console.log(key.value, value);
      })
    }

    isCyclic(node:Node, visited:boolean[], stack:boolean[]){
      if(stack[node.key]){
        return true;
      }
      if(visited[node.key]){
        return false;
      }
      visited[node.key] = true;
      stack[node.key] = true;
      let canGout = false;

      this.adjList.get(node)?.forEach((edge)=>{
        if(this.isCyclic(edge.terminalB,visited,stack)){
          canGout = true;
        }
      })
      stack[node.key] = false;
      return canGout;
    }

    detectCycle(){
      let visited:boolean[] = new Array(this.adjList.size).fill(false);
      let stack:boolean[] = new Array(this.adjList.size).fill(false);
      let canGout = false;
      this.adjList.forEach((value:Edge[],key:Node)=>{
        if(this.isCyclic(key,visited,stack)){
          canGout = true;
        }
      })
      return canGout;
    }


}


class CircleParent{
    nodeParent:Node;
    circle:Circle;
    constructor(nodeParent:Node,circle:Circle){
      this.circle = circle;
      this.nodeParent = nodeParent;
    }
}
  
function createCircle(nodo:Node, canvas:Svg, left:boolean, timeline:Timeline, radius:number, lenCircus:number, complete:boolean=true){
    let circle = canvas.circle(2*radius).move(2*radius*nodo.x,2*radius*nodo.y);
    circle.fill('#0E1117')
    circle.stroke({
      color: '#203357',
      width: 6,
      linecap: 'round'
    }).timeline(timeline);
    
    if(!complete){
      circle.stroke({
        color: 'f06',
        dasharray: [lenCircus].toString(),
        dashoffset: lenCircus,
      }).fill("none");
    }

    if(!left){
      circle.transform({rotate: 315,scaleY: -1})
    }else{
      circle.transform({rotate: 225});
    }
    
    nodo.circle = circle;
  
    return circle;
  }

  function createCircleNoCopy(nodo:Node, canvas:Svg, left:boolean, timeline:Timeline, radius:number, lenCircus:number, complete:boolean=true){
    let circle = canvas.circle(2*radius).move(2*radius*nodo.x,2*radius*nodo.y);
    circle.fill('#0E1117')
    circle.stroke({
      color: '#203357',
      width: 6,
      linecap: 'round'
    }).timeline(timeline);
    
    if(!complete){
      circle.stroke({
        color: 'f06',
        dasharray: [lenCircus].toString(),
        dashoffset: lenCircus,
      }).fill("none");
    }

    if(!left){
      circle.transform({rotate: 315,scaleY: -1})
    }else{
      circle.transform({rotate: 225});
    }
      
    return circle;
  }
  
function createLetter(nodo:Node, canvas:Svg, timeline:Timeline, txSize:number, radius:number, theme:string){
    let txt = canvas.text(nodo.value.toString()).font({
      family: 'Helvetica', size: txSize, opacity: 1
    })

    if(theme == "dark"){
      txt.fill("white");
    }else{
      txt.fill("black");
    }
    txt.move(2*radius*nodo.x + radius-  (txt.text().length)*(0.5)*(txt.length()/(txt.text().length)),radius/2.5 + 2*radius*nodo.y ).timeline(timeline);
    nodo.letter = txt;
    return txt;
  }

function createLetterEdge(edge:Edge, canvas:Svg | null, timeline:Timeline, txSize:number, radius:number, theme:string){
  if(canvas){
    let txt = canvas.text(edge.weight.toString()).font({
      family: 'Helvetica', size: txSize, opacity: 1
    })

    if(theme == "dark"){
      txt.fill("white");
    }else{
      txt.fill("black");
    }

    if(edge.terminalA.circle && edge.terminalB.circle){
      txt.cx((edge.terminalA.circle?.cx() + 2*edge.terminalB.circle?.cx())/3);
      txt.cy((edge.terminalA.circle?.cy() + 2*edge.terminalB.circle?.cy())/3);
      txt.timeline(timeline);
    }
    edge.letter = txt;
    return txt;
  }else{
    return new Text();
  } 
}
  
function createLine(nodoA:Node, nodoB:Node, timeline:Timeline, radius:number, canvas:Svg | null, setColor:string = "#203357",complete:boolean = true){
    if(canvas){
      let fromNode:number[],toNode:number[];
      let pendiente;
      let newyA,newxA,newyB,newxB;
      let oldyA = 2*radius*nodoA.y+ radius,oldxA=2*radius*nodoA.x + radius;
      let oldyB = 2*radius*nodoB.y+ radius,oldxB=2*radius*nodoB.x + radius;
      if(nodoA.x == nodoB.x){
        pendiente = Infinity;
        newxA = oldxA;
        newxB = oldxB;
        newyB = oldyB + radius;
        newyA = oldyA - radius;
        if(nodoA.y < nodoB.y){
          newyB = oldyB - radius;
          newyA = oldyA + radius;
        }
      }else{
        pendiente = (oldyA - oldyB)/(oldxA - oldxB);
        if(pendiente != 0){
          if(nodoA.x < nodoB.x){
            newyA = oldyA + radius*pendiente/Math.sqrt(1 + pendiente*pendiente);
            newyB = oldyB - radius*pendiente/Math.sqrt(1 + pendiente*pendiente);
          }else{
            newyA = oldyA - radius*pendiente/Math.sqrt(1 + pendiente*pendiente);
            newyB = oldyB + radius*pendiente/Math.sqrt(1 + pendiente*pendiente);
          }
          newxA = oldxA + (newyA - oldyA)/pendiente;
          newxB = oldxB + (newyB - oldyB)/pendiente;
        }else{
          newyA = oldyA;
          newyB = oldyB;
          newxA = oldxA + radius;
          newxB = oldxB - radius;
          if(nodoA.x > nodoB.x){
            newxB = oldxB + radius;
            newxA = oldxA - radius;
          }
        }
      }

      fromNode = [newxA,newyA];
      toNode = [newxB,newyB];
      let ln = canvas.line()
      if(complete){
        ln.plot([fromNode[0],fromNode[1],toNode[0],toNode[1]]).stroke(
          { color: setColor, width: 6, linecap: 'round',opacity: 1 }
        )
      }else{
        ln.plot([fromNode[0],fromNode[1],fromNode[0],fromNode[1]]).stroke(
          { color: setColor, width: 6, linecap: 'round',opacity: 0 }
        )
      }
      
      
      ln.timeline(timeline).remember({
        from : fromNode,
        to : toNode
      });
      return ln;
    }
    return new Line();
  }

function createLineCoords(initPos:number[], lastPos:number[], timeline:Timeline, radius:number, canvas:Svg | null, setColor:string = "#203357",complete:boolean = true){
    if(canvas){
      let ln = canvas.line()
      if(complete){
        ln.plot([initPos[0],initPos[1],lastPos[0],lastPos[1]]).stroke(
          { color: setColor, width: 6, linecap: 'round',opacity: 1 }
        )
      }else{
        ln.plot([initPos[0],initPos[1],initPos[0],initPos[1]]).stroke(
          { color: setColor, width: 6, linecap: 'round',opacity: 0 }
        )
      }
      
      ln.timeline(timeline).remember({
        from : initPos,
        to : lastPos
      });
      return ln;
    }
    return new Line();
  }

function createArrow(edge:Edge,timeline:Timeline,radius:number,canvas:Svg|null, type:boolean, setColor:string="#203357"){
  if(canvas){

    let fromNode:number[],toNode:number[];
    let pendiente;
    let nodoA = edge.terminalA;
    let nodoB = edge.terminalB;
    let newyB,newxB;
    let auxX,auxY;
    let posX,posY;
    let specRadius = radius*Math.sqrt(3)/2;
    let oldyA = 2*radius*nodoA.y+ radius,oldxA=2*radius*nodoA.x + radius;
    let oldyB = 2*radius*nodoB.y+ radius,oldxB=2*radius*nodoB.x + radius;
    if(nodoA.x == nodoB.x){
      pendiente = Infinity;
      auxX = oldxB;
      newxB = oldxB;
      newyB = oldyB + radius;
      auxY = newyB + specRadius;
      if(nodoA.y < nodoB.y){
        newyB = oldyB - radius;
        auxY = newyB - specRadius;
      }
      posY = auxY;
      posX = auxX - radius/2;
      if(type){
        posX = auxX + radius/2;
      }
    }else{
      pendiente = (oldyA - oldyB)/(oldxA - oldxB);
      if(pendiente != 0){
        if(nodoA.x < nodoB.x){
          newyB = oldyB - radius*pendiente/Math.sqrt(1 + pendiente*pendiente);
        }else{
          newyB = oldyB + radius*pendiente/Math.sqrt(1 + pendiente*pendiente);
        }
        newxB = oldxB + (newyB - oldyB)/pendiente;
        if(nodoA.x < nodoB.x){
          auxY = newyB - specRadius*pendiente/Math.sqrt(1 + pendiente*pendiente);
        }else{
          auxY = newyB + specRadius*pendiente/Math.sqrt(1 + pendiente*pendiente);
        }
        auxX = newxB + (auxY - newyB)/pendiente;
        pendiente = -1/pendiente;
        posY = auxY - (radius/2)*pendiente/Math.sqrt(1 + pendiente*pendiente);
        if(type){
          posY = auxY + (radius/2)*pendiente/Math.sqrt(1 + pendiente*pendiente);
        }
        posX = auxX + (posY - auxY)/pendiente;
      }else{
        auxY = oldyB;
        newyB = oldyB;
        newxB = oldxB - radius;
        auxX = newxB  - specRadius;
        if(nodoA.x > nodoB.x){
          newxB = oldxB + radius;
          auxX = newxB + specRadius;
        }
        posX = auxX;
        posY = auxY + radius/2
        if(type){
          posY = auxY - radius/2
        }
      }
    }
    fromNode = [newxB,newyB];
    toNode = [posX,posY];
    let ln = canvas.line()
    ln.plot([fromNode[0],fromNode[1],toNode[0],toNode[1]]).stroke(
      { color: setColor, width: 6, linecap: 'round',opacity: 1 }
    )
    ln.timeline(timeline).remember({
      from : fromNode,
      to : toNode
    });
    return ln;
  }
  return new Line();
}

function onMouseCircle(this: Circle){
  this.fill({ color: '#FF4B4B' }).attr('cursor', 'pointer');
}
//
function outMouseCircle(this: Circle){
  this.fill({ color: '#0E1117' }).attr('cursor', 'default');
}

const GraphKruskal = (props:any) => {
    const svgRef = useRef<HTMLDivElement | null>(null);
    const drawRef = useRef<Svg | null>(null);
    const buttonRef = useRef<HTMLButtonElement | null>(null);
    const [nodeSelect, setNodeSelect] = useState<Node | null>(null);
    const [ciclesMain, setCiclesMain] = useState<CircleParent[] | null>(null);
    const [nodesMain, setNodesMain] = useState<Node[]>([]);
    const [graphMain,setGraphMain] = useState<Graph>(new Graph());


    const {theme, radius, speed} = props;
    const numberOfNodes =6
    const lenCircle = 2*radius*Math.PI;
    const mainWidth = 2*(10)*radius;
    const mainHeight = 2*(7)*radius;

    const buttonOut = {
      display: "block",
      borderStyle: "none",
      border: "2px solid #203357",
      borderRadius: "12%",
      width: "80px",
      backgroundColor: "transparent", 
      color: "white",
      margin: "auto",
      fontSize: "16px"
    }

    const buttonOver = {
      display: "block",
      borderStyle: "none",
      border: "2px solid #FF4B4B",
      borderRadius: "12%",
      width: "80px",
      backgroundColor: "transparent", 
      color: "#FF4B4B",
      margin: "auto",
      fontSize: "16px"
    }

    const handleButtonOver = () => {
      if (buttonRef.current && !buttonRef.current.disabled) {
        Object.assign(buttonRef.current.style, buttonOver);
      }
    };
  
    const handleButtonOut = () => {
      if (buttonRef.current) {
        Object.assign(buttonRef.current.style, buttonOut);
      }
    };
    

  
    function getParent(parent:number[],key:number) : number{
      if(parent[key] == key){
        return key;
      }
      return parent[key] = getParent(parent,parent[key]);
    }

    function unionEdges(nodoA:number,nodoB:number, parent:number[], priority:number[]){
      nodoA = getParent(parent,nodoA);
      nodoB = getParent(parent,nodoB);
      if(priority[nodoA] < priority[nodoB]){
        parent[nodoA] = nodoB;
      }else if(priority[nodoA] > priority[nodoB]){
        parent[nodoB] = nodoA;
      }else{
        parent[nodoB] = nodoA;
        priority[nodoA]++;
      }
    }

    function kruskal(graph:Graph=graphMain){
      if(buttonRef.current){
        buttonRef.current.disabled = true;
      }
      let parent:number[] = [];
      let priority:number[] = [];
      let edgesSet:Set<Edge> = new Set();
      let nodesVisited:Set<Node> = new Set();
      const listSvg:List<Circle | Line>= new List();
      let timer = 0;
      const auxTime = new Timeline().persist(true);
      auxTime.on('finished', (e) => {
        listSvg.forEach((el) => {
          el.remove();
        })
        if(buttonRef.current){
          buttonRef.current.disabled = false;
        }
      })

      graph.adjList.forEach((edgesList)=>{
        edgesList.forEach((edge)=>{
          edgesSet.add(edge)
        })
      })
      let edges:Edge[] = Array.from(edgesSet);
      edges.sort((a,b) => { return a.weight - b.weight});
      for(let i = 0;i<nodesMain.length;i++){
        parent[i]=i;
        priority[i]=0;
      }
      
      for(let i = 0;i<edges.length;i++){
        console.log(edges[i].weight);
        let nodoA:number = getParent(parent,edges[i].terminalA.key);
        let nodoB:number = getParent(parent,edges[i].terminalB.key);
        if(nodoA != nodoB){
          
          
          if(drawRef.current){
            if(!nodesVisited.has(edges[i].terminalA)){
              nodesVisited.add(edges[i].terminalA);
              let cir = createCircleNoCopy(edges[i].terminalA,drawRef.current,false,auxTime,radius,lenCircle,true);
              cir.fill("transparent")
              cir.stroke({color:"blue"});
              cir.opacity(0)
              cir.animate(1,timer + 1000,"absolute").opacity(1)
              listSvg.push(cir);
            }
            if(!nodesVisited.has(edges[i].terminalB)){
              nodesVisited.add(edges[i].terminalB);
              let cir = createCircle(edges[i].terminalB,drawRef.current,false,auxTime,radius,lenCircle,true);
              cir.fill("transparent")
              cir.stroke({color:"blue"});
              cir.opacity(0)
              cir.animate(1,timer + 1000,"absolute").opacity(1)
              listSvg.push(cir);
            }
          }
          


          let ln = createLine(edges[i].terminalA,edges[i].terminalB,auxTime,radius,drawRef.current,"blue",true);
          if(nodesMain[0].circle){
            ln.insertBefore(nodesMain[0].circle)
          }   
          ln.opacity(0);
          timer+=1000;
          ln.animate(1,timer,"absolute").opacity(1);
          listSvg.push(ln);
          unionEdges(nodoA,nodoB,parent,priority);

        
        }else{
          let ln = createLine(edges[i].terminalA,edges[i].terminalB,auxTime,radius,drawRef.current,"red",true);
          if(nodesMain[0].circle){
            ln.insertBefore(nodesMain[0].circle)
          }   
          ln.opacity(0);
          timer+=1000;
          ln.animate(1,timer,"absolute").opacity(1);
          listSvg.push(ln);
          unionEdges(nodoA,nodoB,parent,priority);
        }
      }
      listSvg.forEach((el)=>{
        el.animate(1000,timer,"absolute").opacity(0);
      })
    }

    const myTime = new Timeline().persist(true)
    myTime.on('finished', (e) => {
      myTime.stop();
      myTime.play();
    })

    useEffect(() => Streamlit.setFrameHeight());

    useEffect(() => {
      if (svgRef.current) {
        if(ciclesMain == null){
          const draw = SVG().addTo(svgRef.current).size('100%', '100%');
          drawRef.current = draw;
          let nodes:Node[] = [];
          let circles:CircleParent[] = [];
          nodes.push(new Node('a',1,3,0));
          nodes.push(new Node('b',3,1,1));
          nodes.push(new Node('c',6,1,2));
          nodes.push(new Node('d',8,3,3));
          nodes.push(new Node('e',6,5,4));
          nodes.push(new Node('f',3,5,5));
          for(let i = 0;i<nodes.length;i++){
            graphMain.addNode(nodes[i]);
          }
          graphMain.generateMatrix();
          nodes.forEach((node) => {
            let circle = createCircle(node,draw,true,myTime,radius,lenCircle);
            circles.push(new CircleParent(node,circle));
            createLetter(node,draw,myTime,radius,radius,theme); 
          })
          setCiclesMain(circles);
          setNodesMain(nodes);

        }else{
          ciclesMain.forEach((circleItem)=>{
            circleItem.circle.on("mouseover",onMouseCircle);
            circleItem.circle.on("mouseout",outMouseCircle);
            circleItem.circle.on("click",function(this: Circle){
              if(nodeSelect != null){
                nodeSelect.circle?.stroke("#203357")
                if(nodeSelect != circleItem.nodeParent && !graphMain.existsEdge(nodeSelect,circleItem.nodeParent)){ 
                  let valEdge = prompt("Ingrese el peso de la arista: ","1");
                  if(Number(valEdge) && Number(valEdge) > 0){
                    let newEdge = new Edge(nodeSelect,circleItem.nodeParent,Number(valEdge))
                    let txEdge = createLetterEdge(newEdge,drawRef.current,myTime,3*radius/4,3*radius/4,theme);
                    let line = createLine(nodeSelect,circleItem.nodeParent,myTime,radius, drawRef.current,);
                    line?.back();
                    if(line){
                      newEdge.line = line;
                    }
                    graphMain.addEdge(newEdge);
                    line?.on("mouseover",function(this:Line){
                      this.stroke({ color: '#FF4B4B' }).attr('cursor', 'pointer');
                    });
                    line?.on("mouseout",function(this:Line){
                      this.stroke({ color: '#203357' }).attr('cursor', 'default');
                    });
                    line?.on("click",function(this:Line){
                      this.remove();
                      txEdge.remove();
                      graphMain.deleteEdge(newEdge);
                    })
                  }else{
                    alert("Ingrese un numero positivo")
                  }
                }
                
                setNodeSelect(null);
              }else{
                setNodeSelect(circleItem.nodeParent);
                this.stroke({color: "#FF4B4B"});
              }
              
            })
          })
        }

        return () => {
          graphMain.printList();
          if(ciclesMain){
            ciclesMain.forEach((circleItem)=>{
              circleItem.circle.off("mouseover");
              circleItem.circle.off("mouseout");
              circleItem.circle.off("click");
            })
          }
        };
      }
    }, [nodeSelect,theme,ciclesMain, nodesMain]);
    

    return (
      <>
        <div ref={svgRef} style={{ width: mainWidth.toString() + "px", height: mainHeight.toString() + "px", margin: "auto"}}>
        </div>
        <button ref = {buttonRef} onClick={()=>{kruskal()}} onMouseOver={handleButtonOver} onMouseOut={handleButtonOut} style={buttonOut} >Kruskal</button>       
      </>
    );
  };
  
  export default GraphKruskal;