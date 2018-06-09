package com.example.tourismfraudprevention;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;

public class GonglueZong extends Activity{
	private ActionBar bar;
	private ListView list;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.gonglue_zong);
		bar=getActionBar();
		bar.hide();
		list=(ListView)findViewById(R.id.gonglue_display);
		list.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> arg0, View arg1, int arg2,
					long arg3) {
				Intent intent = new Intent(GonglueZong.this,GonglueMoban.class);
				intent.setFlags(arg2);
				startActivity(intent);
			}
		});
		
}

	public void gonglue_zong(View view){
		int id = view.getId();
		switch (id) {
		case R.id.gonglue_zong_fanhui:
			startActivity(new Intent(this,MainActivity.class));
			this.finish();
			break;
		}
	}
}
	