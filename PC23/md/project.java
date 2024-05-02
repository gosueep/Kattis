import java.io.*;
import java.nio.*;
import java.nio.channels.FileChannel;
//import java.util.Scanner;

//import javax.management.RuntimeErrorException;

public class project {
    public static int[] arrayLetters = new int[26];
        
    public static byte[] parseInputFile(String inputFile) throws IOException {
        File file = new File(inputFile);
        try (FileChannel fileChannel = new FileInputStream(file).getChannel()) {
            byte[] barray = new byte[(int) file.length()];
            ByteBuffer bb = ByteBuffer.wrap(barray);
            fileChannel.read(bb);
            return barray;
        }
    }
    
    
    
    public static int cores = Runtime.getRuntime().availableProcessors();
    public static void main(String []args){
       // System.out.println(cores);
        
        try{
            String filename = args[0];    
            byte[] arrayName = parseInputFile(filename);
            System.out.println(arrayName.length);
            for(byte c: arrayName){
                
                    // check if newline
                    // if (c == 10){
                    //     break;
                    // }
                    
                    //int indexX = c + 2;
                     System.out.println(c);
                    //arrayLetters[index] +=1;
                }

            for(char c ='a'; c <= 'z'; c++){

                //System.out.println(c + ": " + arrayLetters[c-97]);
            
            }


            }
    
        catch(IOException e){
            throw new RuntimeException(e);
            // System.out.println("balls");

                }   

            }
        
    
}
    
    