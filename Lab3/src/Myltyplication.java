public class Myltyplication {

    public static int[][] multy(int[][] mx, int[][] my){
        int[][] res = new int[mx.length][mx.length];
        for(int i=0;i<mx.length;i++) {
            for (int j = 0; j < mx.length; j++) {
                res[i][j] = 0;
                for (int k = 0; k < mx.length; k++) {
                    res[i][j] += mx[k][i] * my[j][k];
                }
            }
        }
        return res;
    }
    public static Matrix multy(Matrix mx, Matrix my){
        int[][] res = multy(mx.getMatr(), my.getMatr());
        return new Matrix(res);
    }
    public static int[][] quickMulty(int[][] mx, int[][] my){
        if(mx.length%4!=0){
            return multy(mx, my);
        }
        if(mx.length!=my.length){
            return new int[0][0];
        }

        //TODO
        return new int[0][0];
    }
    public static Matrix quickMulty(Matrix mx, Matrix my){
        int[][] res = quickMulty(mx.getMatr(), my.getMatr());
        return new Matrix(res);
    }
}
