import java.util.Set;
import java.util.TreeSet;
// public class "Main"
public class Main {
    public static void main(String[] args) {
        //Inicio de string
        String text = "ICPCCIP";
        //String original
        int originalChain = text.length();
        char[] Cadena = text.toCharArray();
        Set<Character> conjunto = new TreeSet<>();

        for (char C : Cadena) {
            conjunto.add(C);
        }

        StringBuilder pnoduply = new StringBuilder();
        for (char C : conjunto){
            pnoduply.append(C);
        }

        int fixcchain = pnoduply.length();

        int tamañosecuenciaA = originalChain - fixcchain;
                System.out.println(tamañosecuenciaA);

    }
}
