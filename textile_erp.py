class Loom:
    # Class Attribute: Shared by ALL looms in the factory
    factory_name = "Surat GIDC Alpha Mill"
    total_meters_produced = 100

    def __init__(self, loom_id, worker_name):
        self.loom_id = loom_id
        self.worker_name = worker_name
        self._meters = 0  # Private variable (The 'Grey' fabric count)

    # 1. THE GETTER: Accessing the data safely
    @property
    def meters(self):
        print(f"Reading meter for Loom {self.loom_id}...")
        return self._meters

    # 2. THE SETTER: Validating data (Preventing 'Tampering')
    @meters.setter
    def meters(self, value):
        if value < self._meters:
            print("Error: Production cannot go backwards! Potential tampering detected.")
        else:
            # Update the global factory count
            Loom.total_meters_produced += (value - self._meters)
            self._meters = value
            print(f"Successfully updated Loom {self.loom_id} to {value} meters.")

    # 3. CLASS METHOD: Factory-wide statistics
    @classmethod
    def get_factory_report(cls):
        return f"--- {cls.factory_name} Report ---\nTotal Meters: {cls.total_meters_produced}"

# 4. INHERITANCE: Creating a 'Smart' version of the Loom
class SmartLoom(Loom):
    def __init__(self, loom_id, worker_name, ai_version, base_pay):
        super().__init__(loom_id, worker_name)
        self.ai_version = ai_version
        self.base_pay = base_pay # Base salary regardless of work

    def get_total_pagar(self, rate_per_meter=10):
        # Salary = Base Pay + (Meters Produced * Rate)
        # We use 'self.meters' to trigger the Getter we built!
        total = self.base_pay + (self.meters * rate_per_meter)
        return f"Worker {self.worker_name} Total Pagar: ₹{total}"
    
    def run_defect_check(self):
        return f"AI Version {self.ai_version} scanning for oil stains on Loom {self.loom_id}..."

# --- EXECUTION ---
smart_loom_1 = SmartLoom(202, "Amit", "v1.0-Vision", 500) # 500 is base pay
smart_loom_1.meters = 150 # Update production
print(smart_loom_1.get_total_pagar()) # Calculate based on 150 meters

# Try to set meters (The Setter kicks in)
Loom.meters = 50 
Loom.meters = 40  # This will trigger the "Tampering" error

# Create a SmartLoom (Inheritance)
smart_loom_1 = SmartLoom(202, "Amit", "v1.0-Vision", 500)
smart_loom_1.meters = 100

print(smart_loom_1.run_defect_check())
print(Loom.get_factory_report())