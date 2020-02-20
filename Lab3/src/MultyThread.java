public class MultyThread extends Thread {
    private int[][] mx;
    private int[][] my;
    private int n;
    private int[][] res;

    MultyThread(int[][] mx, int[][] my, int n){
        super();
        this.n = n;
        this.my = new int[my.length][my.length];
        this.mx = new int[mx.length][mx.length];
        for (int i=0; i<mx.length; i++){
            for(int j=0; j<mx.length;j++){
                this.mx[i][j] = mx[i][j];
            }
        }
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
                for(int t=0; t<my.length; t++){
                    res[i][j] += my[j][t]*mx[t][n-1];
                }
            }
        }
    }

    public int[][] getRes(){
        return res;
    }
}
