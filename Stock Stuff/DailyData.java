public class DailyData {
	String date;
	double open, high, low, close;
	int volume;

	public DailyData(String date, double open, double high, double low, double close, int volume) {
		this.date   = date;
		this.open   = open;
		this.high   = high;
		this.low    = low;
		this.close  = close;
		this.volume = volume;
	}

	public String toString() {
		return date+" "+open+" "+high+" "+low+" "+close+" "+volume;
	}



}
