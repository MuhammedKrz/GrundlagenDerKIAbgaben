import java.util.BitSet;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Problem8Queens problem8Queens = new Problem8Queens();
        System.out.println(problem8Queens.bitString1.toString());
    }
}

class Problem8Queens {
    BitSet bitString1 = new BitSet(24);
    BitSet bitString2 = new BitSet(24);
    Random randomBoolean = new Random();
    public Problem8Queens() {
        for(int i = 0; i < bitStringValues.length(); i++){
            boolean random = randomBoolean.nextBoolean();
            bitString1.set(i, random);
        }
        for(int i = 0; i < bitStringValues.length(); i++){
            boolean random = randomBoolean.nextBoolean();
            bitString2.set(i, random);
        }
    }
}