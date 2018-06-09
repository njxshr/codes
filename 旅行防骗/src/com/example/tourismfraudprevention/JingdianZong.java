package com.example.tourismfraudprevention;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AdapterView.OnItemSelectedListener;
import android.widget.ListView;
import android.widget.Spinner;

public class JingdianZong extends Activity{
	private ActionBar bar;
	private Spinner spinner;
	private ArrayAdapter<String> adapter;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.jingdian_zong);
		bar=getActionBar();
		bar.hide();
		
		String[] array = getResources().getStringArray(R.array.chengshi);
		
		spinner = (Spinner)findViewById(R.id.spinner_chengshi);
		//将Spinner里面的可选择内容通过ArrayAdapter连接起来  
        adapter=new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item,array);    
        //为Spinner设置适配器  
        spinner.setAdapter(adapter); 
        spinner.setOnItemSelectedListener(new OnItemSelectedListener() {
			@Override
			public void onItemSelected(AdapterView<?> arg0, View arg1,
					int arg2, long arg3) {
				if(arg2==1){
					startActivity(new Intent(JingdianZong.this,JingdianTaiyuan.class));
				}
				if(arg2==2){
					startActivity(new Intent(JingdianZong.this,JingdianDatong.class));
			}
				if(arg2==3){}	
			}

			@Override
			public void onNothingSelected(AdapterView<?> arg0) {
				// TODO Auto-generated method stub
				
			}
		});
		
	}
	
	
	
	
	public void jingdian_zong(View view){
		int id = view.getId();
		switch (id) {
		case R.id.jingdian_zong_fanhui:
			startActivity(new Intent(this,MainActivity.class));
			this.finish();
			break;

		}
	}
	
	
}
