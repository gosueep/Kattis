import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.*;

public class SharingData {
    public static int upperBound = 20_000_000;
    
    private static Lock lock = new ReentrantLock();
    
    
    
    public static int counter = 0;
    public static void incrementLock(String name) {
        for (int i = 0; i < 10_000_000; i++) {
            lock.lock ();
            counter = counter + 1;
            lock.unlock ();
        }
    }
    public static AtomicInteger counteratomic = new AtomicInteger (0);
        public static void increment (String name) {
        System.out.printf("%s: begin\n", name);
        for (int i = 0; i < 10_000_000; i++)
        counteratomic.incrementAndGet();
        System.out.printf("%s: done\n", name);
    }

    public static void main(String[] args) throws Exception {
        counter = 0;

        long start = System.currentTimeMillis();
        
        ExecutorService executor = Executors.newFixedThreadPool(2);
        Future<?> f1 = executor.submit(() -> incrementLock("A"));
        Future<?> f2 = executor.submit(() -> incrementLock("B"));
        f1.get();
        f2.get();
        executor.shutdown();

        // System.out.println(counter);
        System.out.println(System.currentTimeMillis() - start);
    }
}
