package com.example.tourismfraudprevention;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class GonglueMoban extends Activity{
	private String[] files={"gonglue_shizhao"};
	private ActionBar bar;
	private TextView txt;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.gonglue_moban);
		bar= getActionBar();
		bar.hide();
		
		txt=(TextView) findViewById(R.id.gonglue_moban_text);
		
		Intent intent=getIntent();
		int index=intent.getFlags();
		String result =inRead(files[index]);
		txt.setText(result);
	}
	
	public String inRead(String path){
		String t="";
		BufferedReader br=null;
		try {
			br=new BufferedReader(new InputStreamReader(TripPlaceDetailActivity.class.getResourceAsStream("details/"+path+".txt"),"GBK"));
			String len="";
			while((len=br.readLine())!=null){
				t=t+len+"\n";
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally{
			try {
				if(br!=null) br.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return t;
	}
	
	public void gonglue_moban(View view){
		int id = view.getId();
		switch (id) {
		case R.id.gonglue_moban_fanhui:
			startActivity(new Intent(this,GonglueZong.class));
			this.finish();
			break;

		}
	}
}
