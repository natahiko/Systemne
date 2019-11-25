public class Main {

    public static void main(String[] args0) throws InterruptedException {
        int[][] mx = Reader.readMatr("m3.txt");
        int[][] my = Reader.readMatr("m4.txt");

        if(mx.length%4!=0 || mx.length!=my.length){
            System.out.println("Uncorect data");
            return;
        }
        long start1 = System.currentTimeMillis();
        int[][] slow = Myltyplication.multy(mx, my);
        long end1 = System.currentTimeMillis();

        System.out.println("Slow reault: ");
        Matrix.print(slow);
        System.out.println("Slow time: "+(end1-start1)+" milis");
        System.out.println();

        MultyThread tr1 = new MultyThread(mx,my,1);
        MultyThread tr2 = new MultyThread(mx,my,2);
        MultyThread tr3 = new MultyThread(mx,my,3);
        MultyThread tr4 = new MultyThread(mx,my,4);

        long start2 = System.currentTimeMillis();
        tr1.start();
        tr2.start();
        tr3.start();
        tr4.start();
        long end2 = System.currentTimeMillis();

        System.out.println("Quick reault: ");
        MultyThread.sleep(2000);
        Matrix.print(tr1.getRes());
        Matrix.print(tr2.getRes());
        Matrix.print(tr3.getRes());
        Matrix.print(tr4.getRes());
        System.out.println("Quick time: "+(end2-start2)+" milis");
    }
}
