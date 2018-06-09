package com.example.tourismfraudprevention;

import android.app.ActionBar;
import android.app.Activity;
import android.os.Bundle;

public class JingdianKuangjia extends Activity{
	private ActionBar bar;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.jingdian_kuangjia);
		bar=getActionBar();
		bar.hide();
	}
}
