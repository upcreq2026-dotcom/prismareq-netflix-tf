(function(root,factory){const api=factory();if(typeof module==='object')module.exports=api;else root.PrismareqModel=api;})(typeof window!=='undefined'?window:this,function(){
 'use strict';
 return {
  filter(catalog,filters={}){return catalog.filter(t=>t.available && (!filters.theme || t.theme===filters.theme) && (!filters.approach || t.approach===filters.approach));},
  planView(account){return {plan:account.plan,amount:account.amount==null?'No disponible':account.amount,currency:account.currency,limit:account.limit==null?'Límite no disponible':String(account.limit),status:account.status};},
  save(preferences,account,selection,confirmed){const next={...preferences};if(confirmed)next[account]={theme:selection.theme||'',approach:selection.approach||''};return next;},
  remove(preferences,account,confirmed){const next={...preferences};if(confirmed)delete next[account];return next;},
  group(catalog,records){return {seen:catalog.filter(t=>records.seen.includes(t.id)),pending:catalog.filter(t=>records.pending.includes(t.id))};}
 };
});
