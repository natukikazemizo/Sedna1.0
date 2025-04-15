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

    public Velocity getSpeed() {
        return new Velocity();
    }
}
