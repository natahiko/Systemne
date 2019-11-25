public class Matrix {
    private int[][] matr;

    public Matrix(int len){
        matr = new int[len][len];
        for(int i=0; i<len; i++){
            for(int j=0; j<len; i++){
                matr[i][j] = 0;
            }
        }
        return;
    }
    public Matrix(int[][] mx){
        int len = mx.length;
        matr = new int[len][len];
        for(int i=0; i<len; i++){
            for(int j=0; j<len; i++){
                matr[i][j] = mx[i][j];
            }
        }
        return;
    }
    public void print(){
        for(int i=0; i<matr.length; i++){
            for(int j=0; j<matr[i].length; j++){
                System.out.print(matr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void print(int[][] matr){
        for(int i=0; i<matr.length; i++){
            for(int j=0; j<matr[i].length; j++){
                System.out.print(matr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void print(int[][] matr, int n){
        System.out.println("n: "+n);
        for(int i=0; i<matr.length; i++){
            for(int j=0; j<matr[i].length; j++){
                System.out.print(matr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public int[][] getMatr(){
        return matr;
    }
    public int getSize(){
        return matr.length;
    }
}
