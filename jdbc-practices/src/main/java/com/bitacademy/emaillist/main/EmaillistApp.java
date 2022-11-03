package com.bitacademy.emaillist.main;

import java.util.List;
import java.util.Scanner;

import com.bitacademy.emaillist.dao.EmaillistDao;
import com.bitacademy.emaillist.vo.EmaillistVo;

public class EmaillistApp {
	private static Scanner scanner = null;

	public static void main(String[] args) {
		scanner = new Scanner(System.in);

		while (true) {
			System.out.println("(l)ist (a)dd (d)elete (q)uit > ");
			String command = scanner.nextLine();

			if ("l".equals(command)) {
				doList();
			} else if ("a".equals(command)) {
				doAdd();
			} else if ("d".equals(command)) {
				doDelete();
			} else if ("q".equals(command)) {
				break;
			}

		}
		
		scanner.close();

	}

	private static void doDelete() {
		System.out.print("삭제할 이메일:");
		String email = scanner.nextLine();
		
		Boolean list = new EmaillistDao().deleteByEmail(email);
		System.out.println("=====================================");
		doList();
	}

	private static void doAdd() {
		
		System.out.print("성: ");
		String firstName = scanner.nextLine();
		
		System.out.print("이름: ");
		String lastName = scanner.nextLine();
		
		System.out.print("이메일: ");
		String email = scanner.nextLine();
		
		System.out.println(firstName + ":" + lastName + ":" + email);
		System.out.println("=====================================");
		Boolean list = new EmaillistDao().insert(firstName, lastName, email);
		doList();
		
	}

	private static void doList() {
		List<EmaillistVo> list = new EmaillistDao().findAll();
		for(EmaillistVo vo : list) {
			System.out.println("이름: " + vo.getFirstName() + " " + vo.getLastName() + ", 이메일: " + vo.getEmail() );
		}
		
	}

}
