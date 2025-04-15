package java.study.class_diagram.connector.composition;


/**
 * キツネ
 * -------------------
 * 
 */
public class Fox {
    private Tail tail;

    public Fox(Tail tail) {
        this.tail = tail;
    }

    public void run(){
        tail.wave();
    }
}
