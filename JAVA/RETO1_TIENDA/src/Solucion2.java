public class Solucion2 {

    public static int [] reporte(int [] compra){
        int len = compra.length;
        int total = 0;
        int [] resultado = new int[3];
//
        for(int i = 0; i < len; i++) {
            total += compra[i];
        }

        // Ordenamiento del arreglo
        for(int i = 0; i < len; i++) {
            for(int j = i; j < len; j++) {
                if (compra[i] > compra[j]) {
                    int aux = compra[j];
                    compra[j] = compra[i];
                    compra[i] = aux;
                }
            }
        }
        // i = 0 i++ i = 1
//        2700,9500,300,15000,1800,10000,400,3000,400

        resultado[0] = total;
        resultado[1] = compra[0];
        resultado[2] = compra[len - 1];

        return resultado;
    }
/*
    public static void main(String[] args) {
        int[] compra = {6700};
        int[] resultado = Solucion2.reporte(compra);


        for(int r: resultado){
            System.out.println(r);
        }

    }*/
}
