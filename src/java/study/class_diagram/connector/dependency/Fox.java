package java.study.class_diagram.connector.dependency;

/**
 * キツネ
 * -------------------
 * 
 */
public class Fox {

    public Fox() {

    }

    public void run(){}

    public Leaf getSpeed() {
        return new Leaf();
    }
}
