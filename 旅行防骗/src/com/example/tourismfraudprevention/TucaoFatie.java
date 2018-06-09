package com.example.tourismfraudprevention;

import java.util.Calendar;

import com.example.tourismfraudprevention.dao.PostDao;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class TucaoFatie extends Activity{
	private ActionBar bar;
	private EditText theme,cont;
	private PostDao db;
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.tucao_fatie);
		bar=getActionBar();
		bar.hide();
		
		db=new PostDao(this);
		
		theme=(EditText) findViewById(R.id.fatie_miaoti);
		cont=(EditText) findViewById(R.id.fatie_zhengwen);
		
	}
	public void fatie_btn(View view){
		int id = view.getId();
		switch(id){
		case R.id.fanhui:
		onBackPressed();
		break;
		case R.id.fabiao:{
			if(DengluZhanghao.isLogin){
				String the=theme.getText().toString();
				String con=cont.getText().toString();
				if("".equals(the)||"".equals(con)){
					Toast.makeText(this, "请输入内容后发表", Toast.LENGTH_SHORT).show();
				}else{
					Calendar c=Calendar.getInstance();
					String date=c.get(Calendar.YEAR)+"-"+(c.get(Calendar.MONTH)+1)+"-"+c.get(Calendar.DAY_OF_MONTH);
					db.insertDB(new String[]{the,con,DengluZhanghao.accountName,date});
					Toast.makeText(this, "发表成功", Toast.LENGTH_SHORT).show();
					onBackPressed();
				}
			}else{
				Toast.makeText(this, "请登录后发帖", Toast.LENGTH_SHORT).show();
				startActivity(new Intent(this,DengluZhanghao.class));
			}
		}
		
		}
 	}
	
	@Override
	public void onBackPressed() {
		startActivity(new Intent(this,TucaoSouyue.class));
		finish();
	}
	
}
