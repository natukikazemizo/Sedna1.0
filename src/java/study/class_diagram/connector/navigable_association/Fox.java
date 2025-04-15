package java.study.class_diagram.connector.navigable_association;


/**
 * キツネ
 * -------------------
 * 
 */
public class Fox {
    private Food lunch;

    public Fox() {

    }

    public void run(){
        eat();
    }

    private void eat() {
        lunch.eaten();
    }
}
