import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Node {
      private int number;
      private double weight;
      public  double g;
      private double h;
      private double f;
      private List<Node> children=new ArrayList<>();
      private List<Node> allParents=new ArrayList<>();
      private Node trackableParent;


    @Override
    public String toString() {
        List<String> childrenList=new ArrayList<>();
        List<String> parentList=new ArrayList<>();
        for (Node node:children
        ) {
            childrenList.add(String.valueOf(node.getNumber()));
        }
        for (Node node:allParents
        ) {
            parentList.add(String.valueOf(node.getNumber()));
        }

        return "Node{" +
                "number=" + number +
                ", weight=" + weight +
                ", g=" + g +
                ", h=" + h +
                ", f=" + f +
                ", children=" + childrenList.toString() +
                ", parents=" + parentList.toString() +
                ", trackableParent=" + trackableParent +
                '}';
    }


    public Node getTrackableParent() {
        return trackableParent;
    }

    public void calculateHeuristics(){
        List<Node> visited=new ArrayList<>();
        DFS(visited,this);
        this.h=visited.size();

    }

    public void  DFS(List<Node> visited, Node node) {
        if (!visited.contains(node)) {
            visited.add(node);
            for (Node child : node.getChildren()) {
                DFS(visited, child);
            }
        }

    }
    public void setTrackableParent(Node trackableParent) {
        this.trackableParent = trackableParent;
    }

    public List<Node> getChildren() {
        return children;
    }
    public List<Node> getAllParents() {
        return allParents;
    }
    public void setChildren(List<Node> children) {
        this.children = children;
    }
    public void addParent(Node parent) {
        this.allParents.add(parent);
    }
    public void addChild(Node child) {
        this.children.add(child);
    }


    public Node(int number) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }


    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public double getG() {
        return g;
    }

    public void setG(double g) {
        this.g = g;
    }

    public double getH() {
        return h;
    }

    public double getF(){return f; }
    public void setF(){
        this.f=this.g+this.h;


    }

}
