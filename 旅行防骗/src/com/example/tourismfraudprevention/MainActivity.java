package com.example.tourismfraudprevention;



import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
	

public class MainActivity extends Activity {
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		//ActionBar
	 	
	}
	 	public void myBtn(View view){
			int id = view.getId();
			switch(id){
			case R.id.tucao:
			Intent intent = new Intent(this,TucaoSouyue.class);
			startActivity(intent);
			break;
			case R.id.jingdian:
				Intent intent1 = new Intent(this,JingdianZong.class);
				startActivity(intent1);
				break;
			case R.id.gonglue:
				Intent intent2 = new Intent(this,GonglueZong.class);
				startActivity(intent2);
				break;
			}
	 	}

	public boolean onCreateOptionsMenu(Menu menu){
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
		
	}
	public void shouye_jingdian(View view){
		int id = view.getId();
		switch (id) {
		case R.id.shouye_jinzhong_mianshan:{
			Intent intent=new Intent(this,TripPlaceFirstActivity.class);
			//这里的Flags值为跳转后对应信息的索引值,目的为了使用同一个Activity显示不同信息
			intent.setFlags(0);
			startActivity(intent);
			finish();
			break;
		}
		case R.id.shouye_yuncheng_pingyaogucheng:{
			Intent intent4=new Intent(this,TripPlaceFirstActivity.class);
			intent4.setFlags(1);
			startActivity(intent4);
			finish();
			break;
		}
		case R.id.shouye_datong_yungangshiku:{
			Intent intent2=new Intent(this,TripPlaceFirstActivity.class);
			intent2.setFlags(2);
			startActivity(intent2);
			finish();
			break;
		}
		case R.id.shouye_xinzhou_wutaishan:{
			Intent intent3=new Intent(this,TripPlaceFirstActivity.class);
			intent3.setFlags(3);
			startActivity(intent3);
			finish();
			break;
		}
		}
	}
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		switch (item.getItemId()) {
		case R.id.zuce:
			Intent intent1 = new Intent(this,ZuceZhanghao.class);
			startActivity(intent1);
			break;
		case R.id.denglu:
			startActivity(new Intent(this,DengluZhanghao.class));
			break;
		
		}
		return super.onOptionsItemSelected(item);
	}

}