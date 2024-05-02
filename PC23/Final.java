import java.io.*;
import java.nio.*;
import java.nio.channels.FileChannel;

public class Final {

    public static byte[] parseInputFile(String inputFile) throws IOException {
        File file = new File(inputFile);
        try (FileChannel fileChannel = new FileInputStream(file).getChannel()) {
            byte[] barray = new byte[(int) file.length()];
            ByteBuffer bb = ByteBuffer.wrap(barray);
            fileChannel.read(bb);
            return barray;
        }
    }

    public static void main(String[] args) {
        System.out.println(args[0]);


        try {
            byte[] input; 
            input = parseInputFile(args[0]);
            for(byte b : input){
                System.out.println(b);
            }
        } catch(IOException e) {
            System.out.println("error reading file:" + e);
        }


    }
}