import java.util.Arrays;

public class Solucion {

    public static int [] reporte(int [] compra){
        int total = 0;
        int [] resultado = new int[3];
        Arrays.sort(compra);
        
        for(int c: compra){
            total += c;
        }
        resultado[0] = total;
        resultado[1] = compra[0];
        resultado[2] = compra[compra.length - 1];

        return resultado;
    }

    public static void main(String[] args) {
        int[] compra = {2700,9500,300,15000,1800,10000,400,3000,400};
        System.out.println(Arrays.toString(Solucion.reporte(compra)));
    }
}
