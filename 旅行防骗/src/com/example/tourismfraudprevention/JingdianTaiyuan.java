package com.example.tourismfraudprevention;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class JingdianTaiyuan extends Activity{
	private ActionBar bar;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.jingdian_taiyuan);
		bar=getActionBar();
		bar.hide();
	}
	public void jingdian_taiyuan(View view){
		int id = view.getId();
		switch (id) {
		case R.id.jingdian_taiyuan_fanhui:
			startActivity(new Intent(this,JingdianZong.class));
			this.finish();
			break;
		case R.id.jingdian_taiyuan_fenheerku:{
			Intent intent=new Intent(this,TripPlaceDetailActivity.class);
			//这里的Flags值为跳转后对应信息的索引值,目的为了使用同一个Activity显示不同信息
			intent.setFlags(0);
			startActivity(intent);
			finish();
			break;
		}
		case R.id.jingdian_taiyuan_jinci:{
			Intent intent1=new Intent(this,TripPlaceDetailActivity.class);
			intent1.setFlags(1);
			startActivity(intent1);
			finish();
			break;
		}
		case R.id.jingdian_taiyuan_shuangtasi:{
			Intent intent2=new Intent(this,TripPlaceDetailActivity.class);
			intent2.setFlags(2);
			startActivity(intent2);
			finish();
			break;
		}
		case R.id.jingdian_taiyuan_yinzegongyuan:{
			Intent intent3=new Intent(this,TripPlaceDetailActivity.class);
			intent3.setFlags(3);
			startActivity(intent3);
			finish();
			break;
		}
		}
	}
}
