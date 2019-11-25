import java.io.*;

public class Reader{

    public static Matrix readMatrix(String filename){
        int[][] res = readMatr(filename);
        return new Matrix(res);
    }
    public static int[][] readMatr(String filename){
        File file = new File(filename);
        BufferedReader br;
        try{
            br = new BufferedReader(new FileReader(file));
            String line1 = br.readLine();
            int a = Integer.parseInt(line1);

            int[][] res = new int[a][a];
            for(int i=0; i<a; i++){
                String ln = br.readLine();
                String[] arr = ln.split(" ");
                for(int j=0; j<a; j++){
                    res[i][j] = Integer.parseInt(arr[j]);
                }
            }

            return res;
        } catch (Exception e){
            e.printStackTrace();
        }
        return new int[0][0];
    }
}
