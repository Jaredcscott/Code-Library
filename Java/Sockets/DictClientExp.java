import java.io.*;
import java.net.*;

// https://tools.ietf.org/html/rfc2229
public class DictClientExp {
	public static void main(String[] args) throws IOException {
		if (args.length == 0) {
			System.err.println("  usage: java DictClient word1 word2 ...");
			System.err.println("example: java DictClient hello memory");
			return;
		}

		String host = "dict.org";
		int port = 2628;

		SocketAddress sa = new InetSocketAddress(host, port);
		Socket so = new Socket();
		so.setSoTimeout(5000);
		so.connect(sa, 5000);

		InputStream in = so.getInputStream();
		OutputStream out = so.getOutputStream();

		BufferedReader br = new BufferedReader(new InputStreamReader(in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));

		System.out.println(br.readLine());	// banner message "220 ..."
		for (String word : args) {
			System.out.println("\n>>>>>>>> " + word + " <<<<<<<<\n"); 

			bw.write("DEFINE foldoc" + word + "\r\n");
			bw.flush();

			String s;
			while ((s = br.readLine()) != null) {
				System.out.println(s);
				if (s.startsWith("250 ") || s.startsWith("552 "))
					break;
			}
		}
		bw.write("quit\r\n");
		bw.flush();
	}
}