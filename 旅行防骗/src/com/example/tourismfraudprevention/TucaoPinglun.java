package com.example.tourismfraudprevention;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class TucaoPinglun extends Activity{
	private ActionBar bar;
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.tucao_pinglun);
		bar=getActionBar();
		bar.hide();
	}
	public void pinglun_btn(View view){
		int id = view.getId();
		switch(id){
		case R.id.fanhui_pinglun:
		Intent intent = new Intent(this,TucaoFatie.class);
		startActivity(intent);
		break;
		
		
		}
 	}
}
