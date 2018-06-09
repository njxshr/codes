package com.example.tourismfraudprevention;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class JingdianDatong extends Activity{
	private ActionBar bar;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.jingdian_datong);
		bar=getActionBar();
		bar.hide();
	}
	public void jingdian_datong(View view){
		int id = view.getId();
		switch (id) {
		case R.id.jingdian_datong_fanhui:
			startActivity(new Intent(this,JingdianZong.class));
			this.finish();
			break;

		}
	}
}
