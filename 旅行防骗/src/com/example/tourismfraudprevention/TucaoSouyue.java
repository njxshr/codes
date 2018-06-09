package com.example.tourismfraudprevention;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.example.tourismfraudprevention.dao.PostDao;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.TextView;

public class TucaoSouyue extends Activity{
	private ActionBar bar;
	private ListView list;
	private PostDao db;
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.tucao_zong);
		bar=getActionBar();
		bar.hide();
		
		db=new PostDao(this);
		
		list=(ListView) findViewById(R.id.tucao_display);
		setlist();
		
		
	}
		
	public void setlist(){
		List<Map<String, String>> data=new ArrayList<Map<String,String>>();
		Cursor c=db.queryDB();
		while(c.moveToNext()){
			Map<String, String> map=new HashMap<String, String>();
			map.put("_id", c.getInt(0)+"");
			map.put("theme", c.getString(1));
			map.put("name", c.getString(3));
			map.put("date", c.getString(4));
			data.add(map);
		}
		SimpleAdapter adapter=new SimpleAdapter(this, data, R.layout.tucao_list_item, 
				new String[]{"_id","theme","name","date"}, new int[]{R.id._id,R.id.theme,R.id.name,R.id.date});
		list.setAdapter(adapter);
		
		list.setOnItemClickListener(new OnItemClickListener() {
			public void onItemClick(AdapterView<?> arg0, View arg1, int arg2,
					long arg3) {
				Intent toDetail=new Intent(TucaoSouyue.this,TucaoTiezi.class);
				int flag=Integer.parseInt(((TextView)arg1.findViewById(R.id._id)).getText().toString());
				toDetail.putExtra("id", flag);
				startActivity(toDetail);
			}
		});
	}
	
	public void zongfatie_btn(View view){
		 int id = view.getId();
		 switch (id) {
		case R.id.zong_fatie:
			startActivity(new Intent(this,TucaoFatie.class));
			finish();
			break;
		case R.id.tucaozong_fanhui:
			startActivity(new Intent(this,MainActivity.class));
			finish();
			break;
		}
		}
}
