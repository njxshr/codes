package com.example.tourismfraudprevention;

import com.example.tourismfraudprevention.R.drawable;
import com.example.tourismfraudprevention.dao.PostDao;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class TucaoTiezi extends Activity{
	private ActionBar bar;
	private int id,zan_count;
	private PostDao db;
	private EditText theme,content;
	private TextView counts;
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.tucao_tiezi);
		bar=getActionBar();
		bar.hide();
		
		db=new PostDao(this);
		theme=(EditText) findViewById(R.id.tiezi_biaoti);
		content=(EditText) findViewById(R.id.tiezi_zhengwen);
		counts=(TextView) findViewById(R.id.cout);
		
		Intent intent=getIntent();
		id=intent.getIntExtra("id", -1);
		Cursor data=db.queryDB(id+"");
		if(data.moveToNext()){
			theme.setText(data.getString(1));
			content.setText(data.getString(2));
			Cursor zan_data=db.query_zan(id+"");
			if(zan_data.moveToNext()){
				zan_count=Integer.parseInt(zan_data.getString(1));
			}else{
				db.insert_zan(new String[]{id+"","0"});
				zan_count=0;
			}
			counts.setText(zan_count+"");
		}else{
			Toast.makeText(this, "SYSTEM-ERRO", Toast.LENGTH_SHORT).show();
		}
	}
	public void tiezi_btn(View view){
		switch (view.getId()) {
		case R.id.tiezi_fanhui:
			onBackPressed();
			finish();
			break;
		case R.id.button_dianzan:
			zan_count++;
			db.update_zan(new String[]{zan_count+"",id+""});
			counts.setText(zan_count+"");
			view.setEnabled(false);
			view.setBackgroundResource(R.drawable.dianzan_hou1);
			break;
		}
	}
}
