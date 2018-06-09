package com.example.tourismfraudprevention.dao;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteDatabase.CursorFactory;
import android.database.sqlite.SQLiteOpenHelper;

public class AccountDao extends SQLiteOpenHelper{
	private String sql_accounts="create table accounts("
			+ "username primary key,"
			+ "password ,gender ,box1 ,box2 ,box3 ,phone )";
	private String sql_save_account="create table save_account("
			+ "username ,password ,isSave )";
	
	private SQLiteDatabase sdb;
	
	public AccountDao(Context context){
		this(context,"account.db3",null,1);
	}
	
	public AccountDao(Context context, String name, CursorFactory factory,
			int version) {
		super(context, name, factory, version);
		sdb=this.getReadableDatabase();
	}

	@Override
	public void onCreate(SQLiteDatabase db) {
		db.execSQL(sql_accounts);
		db.execSQL(sql_save_account);
	}

	@Override
	public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
		
	}
	
	public void insertDB(String[] data){
		sdb.execSQL("insert into accounts values (?,?,?,?,?,?,?)",data);
	}
	public void insertSDB(String[] data){
		sdb.execSQL("insert into save_account values (?,?,?)",data);
	}
	
	public void deleteSDB(){
		sdb.execSQL("delete from save_account");
	}
	
	public Cursor querySDB(){
		return sdb.rawQuery("select * from save_account ", null);
	}
	
	public Cursor queryDB(String username){
		return sdb.rawQuery("select * from accounts where username=? ", new String[]{username});
	}
}
