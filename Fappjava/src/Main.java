import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Set;
import java.util.TreeSet;


// public class "Main"
public class Main {
    public static void main(String[] args) {
        //Inicio de string via input
        //###########################################//
        //Prelectura
        public String leerArchivo  (String ruta){
            File archivo = null;
            FileReader fr = null;
            BufferedReader BR = null;
            String linea = "";
            try{
                archivo = new  File(G())
            }
        }
        //#############################################//


        //Post lectura
        String text = leerArchivo;
        //String original
        int originalChain = text.length();
        char[] Cadena = text.toCharArray();
        Set<Character> conjunto = new TreeSet<>();
        //Cadena de texto
        for (char C : Cadena) {
            conjunto.add(C);
        }
        //Build String para entrega
        StringBuilder pnoduply = new StringBuilder();
        for (char C : conjunto){
            pnoduply.append(C);
        }
        //Cadena original
        int fixcchain = pnoduply.length();
        //output
        int tamañosecuenciaA = originalChain - fixcchain;
                System.out.println(tamañosecuenciaA);

    }
}
