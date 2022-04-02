import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class main {
    public static List<Node> loadFromFile(String path){
        BufferedReader reader;
        List<Node> nodes= new ArrayList<>();
        int counter=0;
        int numOfNodes=0;
        int index=0;
        try {
            reader = new BufferedReader(new FileReader(path));
            String line = reader.readLine();
            while (line != null) {
                //takes number of nodes and create them and adds to the list
                if(counter==0){
                    numOfNodes=Integer.parseInt(line);
                    for(int i=0;i<numOfNodes;i++){
                        nodes.add(new Node(i));
                    }
                    Node finalNode= new Node(-1);
                    nodes.add(finalNode);
                }


                //adds weight to them in order
                if (counter>0&&counter<=numOfNodes){
                    nodes.get(counter-1).setWeight(Double.parseDouble(line));
                }
                //reads children from line, adds them to nodes in the order, and mark parents at the same time
                if (counter>numOfNodes){
                    List<Node> children= new ArrayList<>();
                    String [] lineArr= line.split(" ");
                    for (int i=0;i<lineArr.length;i++) {
                        //the problem is, we dont have index -1 so the final node has to be handled in the separate case
                        if (Integer.parseInt(lineArr[i])!=-1) {
                            children.add(nodes.get(Integer.parseInt(lineArr[i])));
                            nodes.get(Integer.parseInt(lineArr[i])).addParent(nodes.get(index));
                        }else{
                            children.add(nodes.get(nodes.size()-1));
                            nodes.get(nodes.size()-1).addParent(nodes.get(index));
                        }
                    }
                    nodes.get(index).setChildren(children);
                    index+=1;
                }
                counter+=1;
                line = reader.readLine();
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //adds fake starting node to all nodes that doesn't have parents
        Node startNode= new Node(numOfNodes);
        nodes.add(startNode);
        for (Node child:nodes) {
            if (child.getAllParents().isEmpty() && child!=startNode){
                child.addParent(startNode);
                startNode.addChild(child);
            }
        }

        return nodes;
    }

    public static double A_star(Node startNode){

        List<Node> unvisited = new ArrayList<>();
        List<Node> visited = new ArrayList<>();
        List<Node> parents = new ArrayList<>();

        unvisited.add(startNode);
        while (!unvisited.isEmpty()){
            Node curr=unvisited.get(0);
            //we iterate through all unvisited nodes somewhat related to ones we visited-their children- and we choose the one with a highest f value
            for (Node node:unvisited) {
                if (node.getF()>curr.getF()){
                    curr=node;
                }
            }
            //we add a node with current highest f value to visted list and remove it from unvisited
            unvisited.remove(curr);
            visited.add(curr);

            //if the current node is the last one, so does not have any children, than we trace back to the beggining creating the path we've come
            if(curr.getChildren().isEmpty()){
                while (curr!=null){
                    parents.add(curr);
                    curr=curr.getTrackableParent();
                }


            }else{
                //otherwise we focus on the node's children
                for (Node node:curr.getChildren()) {
                    //if we had already visited it, that we cannot revisit it, so we skip that one
                    if(!visited.contains(node)){
                        //sometimes it might happen that the highest chosen f value belongs to node that has been in unvisited listed for few iterations now. It means, that's its g value will be smaller than the g value and wait of
                        //currently checked node, because we havent come to it so it didn't gain g value
                        double checker=curr.getG()+ curr.getWeight();
                        if (node.getG()<=checker){

                            //if everything is fine we update value of f and g of the child node and add it to the unvisited list so we can choose from it in the next iteration
                            node.setG(curr.getG()+ curr.getWeight());
                            node.setF();
                            node.setTrackableParent(curr);
                            if(!unvisited.contains(node)){
                                unvisited.add(node);
                            }
                        }
                    }
                }
            }
        }
        //calculating the total weight of all nodes added to the traced back road
        double totalWeight=0;
        for (Node node:parents) {
            totalWeight+=node.getWeight();
        }
        return totalWeight;
    }


    public static void main(String[] args) {
        List<String> testFiles=new ArrayList<String>(Arrays.asList("test.txt","test_small.dag","test_small_sparse.dag","test_medium.dag","test_medium_sparse.dag","test_large.dag","test_large_sparse.dag","test_xlarge.dag","test_xlarge_sparse.dag"));
        for (String str:testFiles){
            List<Node> myNodes=loadFromFile(str);
            Node startNode=myNodes.get(myNodes.size()-1);
            double weight=A_star(startNode);
            System.out.println("Weight for path with h=0 for file name: "+str+" is total: "+weight);
            for (Node node:myNodes) {node.calculateHeuristics();}
            double weight2=A_star(startNode);
            System.out.println("Weight for path with DFS heuristics for file name: "+str+" is total: "+weight2);
            System.out.println("=====================================================================================");
        }


    }
}
