from database import SessionLocal
import crud

def test_pipeline():
    print("🔌 Opening a connection to the Docker database...")
    db = SessionLocal()
    
    try:
        print("📝 Attempting to write a test Startup Profile...")
        
        # Using your exact schema column names here:
        new_record = crud.create_startup_profile(
            db=db,
            startup_name="Hangover AI",
            industry="Artificial Intelligence / Ops",
            stage="Hackathon Prototype",
            country="India",
            mission="Building a fully integrated startup organizational memory engine."
        )
        
        print(f"🎉 SUCCESS! Startup Profile created with ID: {new_record.id}")
        print(f"🏢 Company Name: {new_record.startup_name}")
        print(f"🎯 Mission: {new_record.mission}")
        
    except Exception as e:
        print(f"❌ Error encountered: {e}")
        
    finally:
        db.close()
        print("🔌 Connection safely closed.")

if __name__ == "__main__":
    test_pipeline()