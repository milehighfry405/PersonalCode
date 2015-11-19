import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
public class TrendLine {
	
	DailyData[] history;	

	// somehow have the index of the array be compatible with a lookup method
	
	public static void main(String[] args) {
		TrendLine trendline = new TrendLine();
		trendline.readInFile();	
	}
	
	public void readInFile(){
		String filename;
		Scanner in = new Scanner(System.in);
		System.out.println("Please enter the filename of the stock history");
		filename = in.nextLine();
		File file = new File(filename);
		try {
			Scanner scanner = new Scanner(file);
			String line = scanner.nextLine();
			// Get amount of days that the history goes - only going up until  January 3rd, 2000
			int i=0;
			while(scanner.hasNextLine()) {
				i++;
				line = scanner.nextLine();
				String delims = "[,]";
				String[] endDate = line.split(delims);
				if(endDate[0].equals("2000-01-03"))
					break;
			}
				scanner.close();
			// create 2D array to store data
			history = new DailyData[i];
			// reinitialize the file to begenning and read into array
			scanner = new Scanner(file);
			line = scanner.nextLine();
			for(i=0; i<history.length; i++){
				line = scanner.nextLine();
				String delims = "[,]";
				String[] data = line.split(delims);
				String date  = data[0];
				double open  = Double.parseDouble(data[1]);
				double high  = Double.parseDouble(data[2]);
				double low   = Double.parseDouble(data[3]);
				double close = Double.parseDouble(data[4]);
				int volume   = Integer.parseInt(data[5]);
				history[i] = new DailyData(date, open, high, low, close, volume);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	

		for(int i=0; i<20; i++) {
			System.out.println(history[i]);
		}

	}



}
