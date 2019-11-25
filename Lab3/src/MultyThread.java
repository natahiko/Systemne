public class MultyThread extends Thread {
    private int[][] mx;
    private int[][] my;
    private int n;
    private int[][] res;
    private static int[][] res1;
    private static int[][] res2;
    private static int[][] res3;
    private static int[][] res4;

    MultyThread(int[][] mx, int[][] my, int n){
        super();
        this.n = n;
        this.my = new int[my.length][my.length];
        this.mx = new int[mx.length][mx.length];
        //this.mx = new int[mx.length][mx.length/4];
//        for (int i=0; i<mx.length; i++){
//            for(int j=(n-1)*mx.length/4, jj=0; j<mx.length/4*n;j++, jj++){
//                //System.out.println("i: "+i+", j: "+j);
//                this.mx[i][jj] = mx[i][j];
//            }
//        }
        for (int i=0; i<mx.length; i++){
            for(int j=0; j<mx.length;j++){
                //System.out.println("i: "+i+", j: "+j);
                this.mx[i][j] = mx[i][j];
            }
        }
//        for (int i=(n-1)*mx.length/4, ii=0; i<mx.length/4*n; i++, ii++){
//            for(int j=0; j<mx.length;j++){
//                this.mx[ii][j] = mx[i][j];
//            }
//        }
        for (int i=0; i<my.length; i++){
            for (int j=0; j<my.length; j++){
                this.my[i][j] = my[i][j];
            }
        }
    }

    @Override
    public void run()
    {
        res = new int[my.length/4][my.length];
        for(int i=0; i<my.length/4; i++){
            for (int j=0; j<my.length; j++){
                res[i][j] = 0;
                //System.out.print("res["+i+"]["+j+"] = ");
                for(int t=0; t<my.length; t++){
                    res[i][j] += my[j][t]*mx[t][n-1];
                    //System.out.print("+"+my[j][t]+"*"+mx[t][n-1]+" ");
                }
                //System.out.println();
            }
        }

    }

    public int[][] getRes(){
        return res;
    }
}
