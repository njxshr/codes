package com.example.tourismfraudprevention;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import android.os.Bundle;
import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class TripPlaceDetailActivity extends Activity {
	private String[] title=new String[]{"title_fenheerku","title_jinci","title_shuangtasi","title_yinzegongyuan"};
	private int[] images=new int[]{R.drawable.jingdian_taiyuan_fenheerku,R.drawable.jingdian_taiyuan_jinci,R.drawable.jingdian_taiyuan_shuangtasi,R.drawable.jingdian_taiyuan_yinzegongyuan};
	private String[] content=new String[]{"content_fenheerku","content_jinci","content_shuangtasi","content_yinzegongyuan"};
	
	private int index=-1;
	
	private TextView tv1,tv2;
	private ImageView iv1;
	private ActionBar bar;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.jingdian_kuangjia);
		
		bar=getActionBar();
		bar.hide();
		
		Intent intent=getIntent();
		index=intent.getFlags();
		
		if(index==-1){
			Toast.makeText(this, "Êý¾Ý´íÎó", Toast.LENGTH_SHORT).show();
			finish();
		}
		iv1=(ImageView) findViewById(R.id.detail_image);
		tv1=(TextView) findViewById(R.id.detail_title);
		tv2=(TextView) findViewById(R.id.detail_content);
		
		iv1.setImageResource(images[index]);
		tv1.setText(inRead(title[index]));
		tv2.setText(inRead(content[index]));
	}
	public void jingdian_kuangjia(View view){
		int id = view.getId();
		switch (id) {
		case R.id.jingdian_kuangjia_fanhui:
			startActivity(new Intent(this,JingdianZong.class));
			this.finish();
			break;

		}
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
}
