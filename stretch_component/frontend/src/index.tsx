import React from "react";
import ReactDOM from "react-dom";
import {ComponentProps, withStreamlitConnection, Streamlit} from "streamlit-component-lib";
import componentMap from './componentMap';


const myComponent = (props: ComponentProps) =>{
  const {id,type,theme,radius,speed,numberOfNode,key} = props.args;
  const component = componentMap[id];
  console.log(id,component);
  if (component === undefined) {
    return <></>
} else {
    if(id == 'defaultGraph'){
      return component({type, theme,radius,speed,numberOfNode})
    }
    
    return component({theme,radius,speed,numberOfNode})
}
}

const MyComponent = withStreamlitConnection(myComponent);


ReactDOM.render(
  <React.StrictMode>
    <MyComponent />
  </React.StrictMode>,
  document.getElementById("root")
);