import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.Partitioner;
import org.apache.hadoop.io.Text;

public class TextPartitioner implements Partitioner<Text, Text> 
    {

	@Override
	public int getPartition(Text key, Text value, int numReduceTasks) {
		if (numReduceTasks==0)
			return 0;
		String tempKey = key.toString().toLowerCase();
		int ord = (int)(tempKey.charAt(0)) - (int)(new Character('a').charValue()) ;
		if( ord >= 0 && ord <26 )
			return ord%numReduceTasks;
		else
			return 26%numReduceTasks;
		
	}

	@Override
	public void configure(JobConf arg0) {
		// TODO Auto-generated method stub

	}
}