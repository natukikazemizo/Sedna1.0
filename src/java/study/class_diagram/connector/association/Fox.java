package java.study.class_diagram.connector.association;

/**
 * キツネ
 * -------------------
 * 
 */
public class Fox {
    private Tail tail;
    private Arm arm;

    public Fox() {

    }

    public void run(){
        arm.bend();
        tail.wave();
    }
}
