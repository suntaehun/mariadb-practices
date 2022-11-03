package com.bitacademy.emaillist.test;

import java.util.List;

import com.bitacademy.emaillist.dao.EmaillistDao;
import com.bitacademy.emaillist.vo.EmaillistVo;

public class EmaillistDaoTest {

	public static void main(String[] args) {
		testFindAll();
	}

	private static void testFindAll() {
		List<EmaillistVo> list = new EmaillistDao().findAll();
		for(EmaillistVo vo : list) {
			System.out.println("이름: " + vo.getFirstName() + " " + vo.getLastName() + ", 이메일: " + vo.getEmail() );
		}
	}

}
