import GraphCanvaDirected from "./GraphCanvaDirected";
import GraphCanvaWeighted from "./GraphCanvaWeighted";
import StretchGraph from "./StretchGraph";
import GraphCanva from "./GraphCanva"
import GraphKruskal from "./GraphKruskal";
import GraphDijkstras from "./GraphDijkstras";
import GraphA from "./GraphA";

const componentsMap: any = {
    'directed': GraphCanvaDirected,
    'weighted': GraphCanvaWeighted,
    'stretch': StretchGraph,
    'defaultGraph': GraphCanva,
    'kruskal': GraphKruskal,
    'dijkstras': GraphDijkstras,
    'aSearch': GraphA
}

export default componentsMap