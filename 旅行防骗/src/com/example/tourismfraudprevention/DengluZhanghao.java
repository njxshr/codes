package com.example.tourismfraudprevention;

import com.example.tourismfraudprevention.dao.AccountDao;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.CompoundButton.OnCheckedChangeListener;
import android.widget.EditText;
import android.widget.Toast;

public class DengluZhanghao extends Activity{
	private ActionBar bar;
	private EditText username,password;
	private String isSave;
	private AccountDao db;
	public static boolean isLogin=false;
	public static String accountName;
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.dengluzhanghao);
		bar = getActionBar();
		bar.hide();
		
		db=new AccountDao(this);
		
		username=(EditText) findViewById(R.id.denglu_zhanghao_suru);
		password=(EditText) findViewById(R.id.denglu_mima_suru);
		
		Cursor sresult=db.querySDB();
		if(sresult.moveToNext()){
			if("Y".equals(sresult.getString(2))){
				username.setText(sresult.getString(0));
				password.setText(sresult.getString(1));
			}
		}
		
	}
	public void dengluBtn(View view){
		int id = view.getId();
		switch (id) {
		case R.id.dengluzhanghao_fanhui:
			startActivity(new Intent(this,MainActivity.class));
			this.finish();
			break;
		case R.id.denglu_zhuce:
			startActivity(new Intent(this,ZuceZhanghao.class));
			this.finish();
			break;
		case R.id.denglu_button:
			String name=username.getText().toString();
			String pwd=password.getText().toString();
			Cursor results=db.queryDB(name);
			if(results.moveToNext()){
				if(pwd.equals(results.getString(1))){
					db.deleteSDB();
					db.insertSDB(new String[]{name,pwd,isSave});
					isLogin=true;
					accountName=name;
					Toast.makeText(this, "??????", Toast.LENGTH_SHORT).show();
					finish();
				}else Toast.makeText(this, "???????", Toast.LENGTH_SHORT).show();
			}else{
				Toast.makeText(this, "????????", Toast.LENGTH_SHORT).show();
			}
			break;
		}
	}
}
