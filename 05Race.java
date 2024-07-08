import java.util.ArrayList;
import java.util.List;

public class Main {
    private static int downloadedBytes = 0;

    public static void main(String[] args) throws InterruptedException {
        List<Thread> threads = new ArrayList<>();
        
        for (int i = 0; i < 10; i++) {
            Thread thread = new Thread(new FileDownloader());
            thread.start();
            threads.add(thread);
        }

        for (Thread thread : threads) {
            thread.join();
        }

        System.out.println("Total Downloaded bytes: " + downloadedBytes);
    }
    
    public static class FileDownloader implements Runnable {
        @Override
        public void run() {
            for (int j = 0; j < 10; j++) {
                downloadedBytes++;
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
