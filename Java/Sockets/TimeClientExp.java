import java.io.*;
import java.net.*;
import java.util.*;

// https://tools.ietf.org/html/rfc868
public class TimeClientExp {
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
                System.err.println("  usage: java TimeClient host port");
                System.err.println("example: java TimeClient time.nist.gov 37");
                return;
        }

        String host = args[0];
        int port = Integer.parseInt(args[1]);

        Socket so = new Socket(host, port);
        so.setSoTimeout(5000);

        InputStream in = so.getInputStream();

        long m = 0;
        for (int i = 0; i < 4; i++)
            m = m << 8 | in.read();
        m *= 1000;

        TimeZone tz = TimeZone.getTimeZone("GMT");
        Calendar c = Calendar.getInstance(tz);
        c.set(1900, 0, 1, 0, 0, 0);
        m += c.getTimeInMillis();

        Date d = new Date(m);
        System.out.println(d);
    }
}