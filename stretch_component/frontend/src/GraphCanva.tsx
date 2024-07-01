import React, { useEffect, useState, useRef } from "react";
import { Streamlit, withStreamlitConnection, ComponentProps } from "streamlit-component-lib";
import { SVG , Svg, Timeline, Circle, Text, Line, Color, List} from '@svgdotjs/svg.js'

class Node{
    value:any;
    key:number;
    x:number;
    y:number;
    adjacents:Node | null;
    circle:Circle | null;
    letter:Text | null;
    select:boolean;
    constructor(value:any, x:number, y:number,key:number){
      this.value = value;
      this.key = key;
      this.x = x;
      this.y = y;
      this.adjacents = null;
      this.circle = null;
      this.letter = null;
      this.select = false;
    }
  }

class Edge{
    line:Line | null;
    terminalA:Node;
    terminalB:Node;
    constructor(nodoa:Node,nodob:Node){
        this.line = null;
        this.terminalA = nodoa;
        this.terminalB = nodob;
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
      return this.adjMatrix[nodeA.key][nodeB.key] == 1;
    }

    addEdge(edge:Edge){
      if(!this.existsEdge(edge.terminalA,edge.terminalB)){
        this.adjList.get(edge.terminalA)?.push(edge);
        this.adjList.get(edge.terminalB)?.push(edge);
        this.adjMatrix[edge.terminalA.key][edge.terminalB.key] = 1;
        this.adjMatrix[edge.terminalB.key][edge.terminalA.key] = 1;
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

function onMouseCircle(this: Circle){
  this.fill({ color: '#FF4B4B' }).attr('cursor', 'pointer');
}
//
function outMouseCircle(this: Circle){
  this.fill({ color: '#0E1117' }).attr('cursor', 'default');
}

function onMouseLine(this: Circle){
  this.stroke({ color: '#FF4B4B' }).attr('cursor', 'pointer');
}

function outMouseLine(this: Circle){
  this.stroke({ color: '#203357' }).attr('cursor', 'default');
}

const GraphCanva = (props:any) => {
    const svgRef = useRef<HTMLDivElement | null>(null);
    const drawRef = useRef<Svg | null>(null);
    const startRef = useRef<HTMLSelectElement | null>(null);
    const buttonRef = useRef<HTMLButtonElement | null>(null);
    const [nodeSelect, setNodeSelect] = useState<Node | null>(null);
    const [ciclesMain, setCiclesMain] = useState<CircleParent[] | null>(null);
    const [nodesMain, setNodesMain] = useState<Node[] | null>(null);
    const [graphMain,setGraphMain] = useState<Graph>(new Graph());
    const {type, theme, radius, speed} = props;
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

    const selectOut = {
      outline: "none",
      borderRadius: "12%",
      display: "inline-block",
      borderStyle: "none",
      border: "2px solid #203357",
      width: "80px",
      backgroundColor: "transparent", 
      color: "white",
      margin: " 15px 25px",
      fontSize: "16px",
    }

    const optionsOut = {
      outline: "none",
      display: "block",
      borderStyle: "none",
      border: "2px solid #203357",
      width: "80px",
      backgroundColor: "#0E1117", 
      color: "white",
      margin: "15px",
      fontSize: "16px",
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
  
    
    function handleDFS(graph:Graph=graphMain){
      
      if(buttonRef.current){
        buttonRef.current.disabled = true;
      }
      const visited:boolean[] = new Array(Object.keys(graph.adjList).length).fill(false);
      const stack:Node[][] = [];
      const listSvg:List<Circle | Line>= new List();

      const startLetter = startRef.current?.value;
      let startNode:Node | undefined = new Node(21,0,0,33);
      let timeTaken:number = 0;
      nodesMain?.forEach((node)=>{
        if(node.value==startLetter){
          startNode = node;
        }
      });

      const auxTime = new Timeline().persist(true);
      auxTime.on('finished', (e) => {
        listSvg.forEach((el) => {
          el.remove();
        })
        if(buttonRef.current){
          buttonRef.current.disabled = false;
        }
      })

      if(drawRef.current){
        let cir = createCircle(new Node("-",startNode.x,startNode.y,123),drawRef.current,false,auxTime,radius,lenCircle,false);
        cir.stroke({color:"blue"});
        cir.animate(1000,0,'now').ease('<>').stroke({dashoffset: 0});
        timeTaken+=1000;
        listSvg.push(cir);
      }

      stack.push([startNode,startNode]);
      visited[startNode.key] = true;
      while(stack.length != 0){
        const auxNode: Node[] | undefined= stack.pop();
        if(auxNode?.at(0) != auxNode?.at(1)){
          if(drawRef.current && auxNode){
            if(auxNode[0] && auxNode[1] && !visited[auxNode[0].key]){
              let ln = createLine(auxNode[1],auxNode[0],auxTime,radius,drawRef.current,"blue",false);
              ln.animate(1,0,'after').stroke({opacity:1});
              ln.animate(750,0,'after').ease('<>').plot([ln.remember("from"),ln.remember("to")]);
              timeTaken+=756;
              listSvg.push(ln);
            }
            if(auxNode[0]){
              visited[auxNode[0].key] = true;
              let cir = createCircle(new Node("-",auxNode[0].x,auxNode[0].y,123),drawRef.current,false,auxTime,radius,lenCircle,false);
              cir.stroke({color:"blue"});
              cir.animate(1000,0,'after').ease('<>').stroke({dashoffset: 0});
              listSvg.push(cir);
              timeTaken+=1000;
            }
          }
        }
        


        if(auxNode){
          const auxEdges = graph.adjList.get(auxNode[0]);
          auxEdges?.forEach((edge)=>{
            let neightbor:Node;
            let origin:Node;
          
            if(edge.terminalA == auxNode[0]){
              neightbor = edge.terminalB;
              origin = edge.terminalA;
            }else{
              origin = edge.terminalB;
              neightbor = edge.terminalA;
            }

            if(!visited[neightbor.key]){
              stack.push([neightbor,auxNode[0]]);
            }

          })
        }
      }
      
      listSvg.forEach((el)=>{
        el.animate(1000,timeTaken,"absolute").opacity(0);
      })

    }

    function handleBFS(graph:Graph=graphMain){
      if(buttonRef.current){
        buttonRef.current.disabled = true;
      }
      const queue:Node[] = [];
      const listSvg:List<Circle | Line>= new List();
      const visited:boolean[] = new Array(Object.keys(graph.adjList).length).fill(false);
      const startLetter = startRef.current?.value;
      let startNode:Node | undefined = new Node(21,0,0,33);
      let timeTaken:number = 0;
      nodesMain?.forEach((node)=>{
        if(node.value==startLetter){
          startNode = node;
        }
      });

      const auxTime = new Timeline().persist(true);
      auxTime.on('finished', (e) => {
        listSvg.forEach((el) => {
          el.remove();
        })
        if(buttonRef.current){
          buttonRef.current.disabled = false;
        }
      })

      visited[startNode.key] = true;
      queue.push(startNode);

      if(drawRef.current){
        let cir = createCircle(new Node("-",startNode.x,startNode.y,123),drawRef.current,false,auxTime,radius,lenCircle,false);
        cir.stroke({color:"blue"});
        cir.animate(1000,0,'now').ease('<>').stroke({dashoffset: 0});
        timeTaken+=1000;
        listSvg.push(cir);
      }

      while(queue.length !== 0){
        const auxNode:Node|undefined = queue.shift(); 
        console.log("Current node: " + auxNode?.value);
        if(auxNode){
          const auxEdges = graph.adjList.get(auxNode);
          auxEdges?.forEach((edge) => {
            let neightbor:Node;
            let origin:Node;
          
            if(edge.terminalA == auxNode){
              neightbor = edge.terminalB;
              origin = edge.terminalA;
            }else{
              origin = edge.terminalB;
              neightbor = edge.terminalA;
            }
   
            if(!visited[neightbor.key]){
              let ln = createLine(origin,neightbor,auxTime,radius,drawRef.current,"blue",false);
              ln.animate(1,0,'after').stroke({opacity:1});
              ln.animate(756,0,'after').ease('<>').plot([ln.remember("from"),ln.remember("to")]);
              timeTaken+=756;
              listSvg.push(ln);
              visited[neightbor.key] = true;
              queue.push(neightbor);
              if(drawRef.current){
                let cir = createCircle(new Node("-",neightbor.x,neightbor.y,123),drawRef.current,false,auxTime,radius,lenCircle,false);
                cir.stroke({color:"blue"});
                cir.animate(1000,0,'after').ease('<>').stroke({dashoffset: 0});
                listSvg.push(cir);
                timeTaken+=1000;
              }
            }
          });
        }  
      }

      listSvg.forEach((el)=>{
        el.animate(1000,timeTaken,"absolute").opacity(0);
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
          nodes.push(new Node('a',1,3,2));
          nodes.push(new Node('b',3,1,0));
          nodes.push(new Node('c',6,1,1));
          nodes.push(new Node('e',6,5,5));
          nodes.push(new Node('d',8,3,3));
          nodes.push(new Node('f',3,5,4));
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
                  let newEdge = new Edge(nodeSelect,circleItem.nodeParent)
                  graphMain.addEdge(newEdge);
                  let line = createLine(nodeSelect,circleItem.nodeParent,myTime,radius, drawRef.current,);
                  line?.back();
                  if(line){
                    newEdge.line = line;
                  }
                  line?.on("mouseover",onMouseLine);
                  line?.on("mouseout",outMouseLine);
                  line?.on("click",function(this:Line){
                    this.remove();
                    graphMain.deleteEdge(newEdge);
                  })
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
              circleItem.circle.off("mouseover",onMouseCircle);
              circleItem.circle.off("mouseout",outMouseCircle);
              circleItem.circle.off("click");
            })
          }
        };
      }
    }, [nodeSelect,theme,ciclesMain, nodesMain]);
    
    const optionItems = nodesMain?.map((node)=>{
      return <option style={optionsOut} value={node.value}>{node.value}</option>
    })
    let buttonRender;
    if(type){
      buttonRender =  <button ref = {buttonRef} onClick={()=>{handleBFS();}} onMouseOver={handleButtonOver} onMouseOut={handleButtonOut} style={buttonOut} >BFS</button>
    }else{
      buttonRender =  <button ref = {buttonRef} onClick={()=>{handleDFS();}} onMouseOver={handleButtonOver} onMouseOut={handleButtonOut} style={buttonOut} >DFS</button>
    }


    return (
      <>
        <div ref={svgRef} style={{ width: mainWidth.toString() + "px", height: mainHeight.toString() + "px", margin: "auto"}}>
        </div>
        {buttonRender}
        <div style={{ width: "100%", display: "flex", justifyContent: "center", alignItems: "center"}}>
          <form>
            <label htmlFor= "nodeStartSelector" style={{display: "inline-block"}}>Vertice origen: </label>
            <select  style={selectOut} ref = {startRef} id="nodeStartSelector" name="nodeStartSelector" required>
                {optionItems}
            </select>
          </form>
          
        </div>
        
      </>
    );
  };
  
  export default GraphCanva ;