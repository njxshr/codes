package com.example.tourismfraudprevention;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class TripPlaceFirstActivity extends Activity{

	private String[] title=new String[]{"title_mianshan","title_pingyaogucheng","title_yungangshiku","title_wutaishan"};
	private int[] images=new int[]{R.drawable.jingdian_jinzhong_mianshan,R.drawable.jingdian_yuncheng_pingyaogucheng,R.drawable.jingdian_datong_yungangshiku,R.drawable.jingdian_xinzhou_wutaishan};
	private String[] content=new String[]{"content_mianshan","content_pingyaogucheng","content_yungangshiku","content_wutaishan"};
	
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
			startActivity(new Intent(this,MainActivity.class));
			this.finish();
			break;

		}
	}
	
	public String inRead(String path){
		String t="";
		BufferedReader br=null;
		try {
			br=new BufferedReader(new InputStreamReader(TripPlaceFirstActivity.class.getResourceAsStream("details/"+path+".txt"),"GBK"));
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
