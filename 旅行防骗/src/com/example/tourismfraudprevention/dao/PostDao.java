package com.example.tourismfraudprevention.dao;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteDatabase.CursorFactory;
import android.database.sqlite.SQLiteOpenHelper;

public class PostDao extends SQLiteOpenHelper{

	private String create_sql="create table post("
			+ "_id integer primary key autoincrement,"
			+ "theme ,context ,username ,date)";
	private String create_zan="create table zan("
			+ "id ,count)";
	
	private SQLiteDatabase sdb;
	
	public PostDao(Context context){
		this(context,"post.db3",null,1);
	}
	
	public PostDao(Context context, String name, CursorFactory factory,
			int version) {
		super(context, name, factory, version);
		sdb=this.getReadableDatabase();
	}

	@Override
	public void onCreate(SQLiteDatabase db) {
		db.execSQL(create_sql);
		db.execSQL(create_zan);
	}

	@Override
	public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
	}
	
	
	public void insertDB(String[] data){
		sdb.execSQL("insert into post(theme ,context ,username ,date) values(?,?,?,?)",data);
	}
	
	public Cursor queryDB(){
		return sdb.rawQuery("select * from post", null);
	}
	
	public Cursor queryDB(String id){
		return sdb.rawQuery("select * from post where _id=?", new String[]{id});
		
	}
	
	public Cursor query_zan(String id){
		return sdb.rawQuery("select * from zan where id=?", new String[]{id});
	}
	
	public void insert_zan(String[] data){
		sdb.execSQL("insert into zan(id,count) values(?,?)",data);
	}
	
	public void update_zan(String[] data){
		sdb.execSQL("update zan set count=? where id=?",data);
	}
}
