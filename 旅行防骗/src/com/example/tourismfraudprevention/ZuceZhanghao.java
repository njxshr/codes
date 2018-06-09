package com.example.tourismfraudprevention;


import com.example.tourismfraudprevention.dao.AccountDao;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.CompoundButton.OnCheckedChangeListener;
import android.widget.EditText;
import android.widget.RadioGroup;
import android.widget.Toast;

public class ZuceZhanghao extends Activity{
	private EditText username,pwd,phone;
	private RadioGroup gendergroup;
	private Button regest;
	private String gender,ischoose1,ischoose2,ischoose3;
	private AccountDao db;
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.zucezhanghao);
		
		username=(EditText) findViewById(R.id.username);
		pwd=(EditText) findViewById(R.id.password);
		phone=(EditText) findViewById(R.id.phone);
		gendergroup=(RadioGroup) findViewById(R.id.gendergroup);
		regest=(Button) findViewById(R.id.btn_zhuce);
		
		db=new AccountDao(this);
		
		ischoose1=ischoose2=ischoose3="N";
		gender="male";
		
		
		
		
		gendergroup.setOnCheckedChangeListener(new android.widget.RadioGroup.OnCheckedChangeListener() {
			public void onCheckedChanged(RadioGroup group, int checkedId) {
				if(checkedId==R.id.male) gender="male";
				else gender="female";
			}
		});
		
		regest.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				String name=username.getText().toString();
				String password=pwd.getText().toString();
				String phonenumber=phone.getText().toString();
				if("".equals(name)||"".equals(password)){
					Toast.makeText(ZuceZhanghao.this, "用户名密码不能为空，请重新输入", Toast.LENGTH_SHORT).show();
				}else{
					if(db.queryDB(name).moveToNext()){
						Toast.makeText(ZuceZhanghao.this, "账号已存在，请重新输入", Toast.LENGTH_SHORT).show();
					}else{
						db.insertDB(new String[]{name,password,gender,ischoose1,ischoose2,ischoose3,phonenumber});
						Toast.makeText(ZuceZhanghao.this, "注册成功", Toast.LENGTH_SHORT).show();
						startActivity(new Intent(ZuceZhanghao.this,DengluZhanghao.class));
					}
				}
			}
		});
	}

}
