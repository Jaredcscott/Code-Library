/**
 * @author Jared Scott ☯
 * 
 */

import java.io.*;
import java.net.*;
import java.util.*;

public class Net {

	static void usage() {
		System.err.println("usage: java Net");
		System.err.println("   or: java Net ifconfig");
		System.err.println("   or: java Net nslookup name");
		System.err.println("   or: java Net ping address");
	}

	public static void main(String[] args) throws IOException {
		if (args.length == 0) {
			InetAddress a = InetAddress.getLocalHost();
			System.out.println("LocalHost: " + a);
			System.out.println("     Name: " + a.getHostName());
			System.out.println("  Address: " + a.getHostAddress());
            usage();
			return;
		}
        
        String op = args[0];
        
        if (op.equals("help") || op.equals("h") || op.equals("--h")) {
			usage();
			return;
		}
            
		if (op.equals("ifconfig")) {
			Enumeration<NetworkInterface> ei = NetworkInterface.getNetworkInterfaces();
			while (ei.hasMoreElements()) {
				NetworkInterface i = ei.nextElement();
				System.out.println(i.getName());
				Enumeration<InetAddress> ea = i.getInetAddresses();
				while (ea.hasMoreElements()) {
					InetAddress a = ea.nextElement();
					System.out.println("    " + a.getHostAddress());
				}
			}
			return;
		}

		if (args.length < 2) {
			usage();
			return;
		}
		
		String s = args[1];

		if (op.equals("nslookup")) {
			InetAddress[] aa = InetAddress.getAllByName(s);
			for (InetAddress a : aa) {
				System.out.println("CanonicalName: " + a.getCanonicalHostName());
				System.out.println("         Name: " + a.getHostName());
				System.out.println("      Address: " + a.getHostAddress());
				System.out.println();
			}
			return;
		}

		if (op.equals("ping")) {
			String[] ss = s.split("\\.");
			if (ss.length != 4) {
				System.err.println("incorrect IPv4 address");
				return;
			}

			byte[] buf = new byte[4];
			for (int i = 0; i < 4; i++) {
				int b = Integer.parseInt(ss[i]);
				if (b < 0 || b > 255) {
					System.err.println("incorrect IPv4 address");
					return;
				}
				buf[i] = (byte) b;
			}

			InetAddress a = InetAddress.getByAddress(buf);
			boolean yes = a.isReachable(10000);
			System.out.println(s + " is " + (yes ? "reachable" : "unreachable"));
			return;
		}
	}
}